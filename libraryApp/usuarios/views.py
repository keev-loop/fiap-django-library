from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmacao_senha = request.POST['confirmacao-senha']

        if not nome.strip():
            messages.error(request, 'Nome não pode ficar em branco')
            return redirect('cadastro')
        if not sobrenome.strip():
            messages.error(request, 'Sobrenome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'Email não pode ficar em branco')
            return redirect('cadastro')
        if not senha.strip():
            messages.error(request, 'Senha não pode ficar em branco')
            return redirect('cadastro')
        if not confirmacao_senha.strip():
            messages.error(request, 'Confirmação de senha não pode ficar em branco')
            return redirect('cadastro')
        if senha != confirmacao_senha:
            messages.error(request, 'Senha e confirmação não podem ser diferentes.')
            return redirect('cadastro')

        User.objects.create_user(first_name=nome, last_name=sobrenome, email=email,
                                 username=f'{nome}.{sobrenome}', password=senha)
        messages.success(request, 'Cadastrado com sucesso!')
        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == '' or senha == '':
            messages.error(request, 'E-mail ou senha devem ser preenchidos')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Login invalido')
    else:
        return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
