from django.shortcuts import render, redirect
from .forms import BinaryTreeNodeForm
from .models import BinaryTreeNode

def create_node(request):
    if request.method == 'POST':
        form = BinaryTreeNodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('node_list')
    else:
        form = BinaryTreeNodeForm()
    
    return render(request, 'create_node.html', {'form': form})

def node_list(request):
    nodes = BinaryTreeNode.objects.all()
    return render(request, 'node_list.html', {'accounts': nodes})
