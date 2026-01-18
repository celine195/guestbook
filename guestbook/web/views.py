from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm

# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']  

# 留言檢視
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    form_class = MessageForm
    success_url = "/"   
    template_name = 'form.html'      

# 刪除留言
class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('web:message_list')              