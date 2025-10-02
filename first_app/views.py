from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView, ListView 
from django.http import HttpResponseRedirect 
from django.utils import timezone 

from .models import Team, Post, Comment 
from .forms import TeamMemberForm, CommentForm, PostForm    

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

# BỔ SUNG: CategoryView để hiển thị danh sách bài viết
class CategoryView(ListView):
    model = Post
    template_name = 'category.html'
    context_object_name = 'object_list'

class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = Team.objects.all() 
        return context

class AddTeamMemberView(CreateView):
    """View để tạo thành viên mới."""
    model = Team
    form_class = TeamMemberForm
    template_name = 'first_app/add_member.html'
    success_url = reverse_lazy('first_app:about')
    
class UpdateTeamMemberView(UpdateView):
    model = Team
    form_class = TeamMemberForm
    template_name = 'first_app/update_member.html'
    success_url = reverse_lazy('first_app:about')

class DeleteTeamMemberView(DeleteView):
    model = Team
    template_name = 'first_app/delete_member.html'
    success_url = reverse_lazy('first_app:about')

# === POST CRUD VIEWS ===

class CreatePostView(CreateView):
    """View để tạo bài viết mới."""
    model = Post
    form_class = PostForm 
    template_name = 'first_app/post_create.html'
    
    # KHẮC PHỤC LỖI CHUYỂN HƯỚNG: PHẢI DÙNG reverse() KHÔNG CÓ _lazy
    def get_success_url(self):
        # self.object là instance của Post vừa được lưu thành công
        return reverse('first_app:single-post', kwargs={'pk': self.object.pk})

class UpdatePostView(UpdateView):
    """View để cập nhật bài viết hiện có."""
    model = Post
    form_class = PostForm
    template_name = 'first_app/post_update.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('first_app:single-post', kwargs={'pk': self.object.pk})

class DeletePostView(DeleteView):
    """View để xóa bài viết."""
    model = Post
    template_name = 'first_app/post_delete.html'
    # Sau khi xóa, chuyển về trang danh mục
    success_url = reverse_lazy('first_app:category') 


class SinglePostView(DetailView):
    """View để xem chi tiết bài viết và thêm bình luận."""
    model = Post
    template_name = 'single-post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Truyền form CommentForm vào context
        context['form'] = CommentForm() 
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 
        form = CommentForm(request.POST) 
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return HttpResponseRedirect(
                # Chuyển hướng lại trang chi tiết bài viết sau khi bình luận thành công
                reverse('first_app:single-post', kwargs={'pk': self.object.pk})
            )
        else:
            # Nếu form không hợp lệ, render lại trang với thông tin post và form có lỗi
            context = self.get_context_data()
            context['form'] = form 
            return self.render_to_response(context)


class CommentUpdateView(UpdateView):
    """View để sửa bình luận."""
    model = Comment
    form_class = CommentForm
    template_name = 'first_app/comment_update.html'
    context_object_name = 'comment'

    def get_success_url(self):
        # Chuyển hướng về trang bài viết chứa bình luận đó
        return reverse('first_app:single-post', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(DeleteView):
    """View để xóa bình luận."""
    model = Comment
    template_name = 'first_app/comment_delete.html'

    def get_success_url(self):
        # Chuyển hướng về trang bài viết chứa bình luận đó
        return reverse_lazy('first_app:single-post', kwargs={'pk': self.object.post.pk})

class ContactView(TemplateView):
    template_name = 'contact.html'
