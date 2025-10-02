from django import forms
from .models import Team, Comment, Post 
from django.utils import timezone

class TeamMemberForm(forms.ModelForm):
    # Form cho TeamMember
    class Meta:
        model = Team
        fields = '__all__' 

class CommentForm(forms.ModelForm):
    # Form cho Comment
    class Meta:
        model = Comment
        fields = ('image', 'author', 'body',)
        widgets = {
            'image': forms.TextInput(attrs={'placeholder': 'URL ảnh đại diện (Tùy chọn)', 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'placeholder': 'Tên của bạn *', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Nhập bình luận của bạn *', 'class': 'form-control', 'rows': 6}),
        }

# POST FORM
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'content', 'author', 'published_date',)
        widgets = {
            # ... (Giữ nguyên các Widgets khác)
            'published_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local', 
                    'class': 'form-control',
                    'value': timezone.now().strftime('%Y-%m-%dT%H:%M')
                },
                # QUAN TRỌNG: Thêm format này
                format='%Y-%m-%dT%H:%M' 
            ),
        }
    
    # BỔ SUNG: Hàm clean để đảm bảo giá trị mặc định nếu người dùng không nhập
    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if published_date is None:
            return timezone.now()
        return published_date