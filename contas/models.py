from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class Profissao(models.TextChoices):
    MEDICO = 'MEDICO', _('Médico')
    PSICOLOGO = 'PSICOLOGO', _('Psicólogo')
    OUTRO = 'OUTRO', _('Outro')

class EspecialidadeMedica(models.TextChoices):
    CARDIOLOGIA = 'CARDIOLOGIA', _('Cardiologista')
    DERMATOLOGIA = 'DERMATOLOGIA', _('Dermatologista')
    GINECOLOGIA = 'GINECOLOGIA', _('Ginecologista')
    PEDIATRIA = 'PEDIATRIA', _('Pediatra')
    PSIQUIATRIA = 'PSIQUIATRIA', _('Psiquiatra')
    PSICOLOGIA = 'PSICOLOGIA', _('Psicologo')
    OUTRO = 'OUTRO', _('Outro')

class UsuarioManager(BaseUserManager):
    """Gerenciador personalizado para o modelo Usuario."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('O email é obrigatório'))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class PessoaProfissional(AbstractBaseUser, PermissionsMixin):
    nome_completo = models.CharField(max_length=100)
    profissao = models.CharField(max_length=20, choices=Profissao.choices)
    endereco = models.TextField()
    celular = models.CharField(max_length=11)
    nome_social = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    especialidade_medica = models.CharField(max_length=20, choices=EspecialidadeMedica.choices)
    foto_documento = models.ImageField(upload_to='contas/fotos_documentos/')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)  # O admin dará permissão após análise do Cadastro
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo', 'cpf', 'celular']

    class Meta:
        verbose_name = _('Pessoa Profissional')
        verbose_name_plural = _('Pessoas Profissionais')
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['cpf']),
        ]

    def __str__(self):
        return self.nome_social
