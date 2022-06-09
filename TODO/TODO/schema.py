import graphene
from graphene_django import DjangoObjectType
from tasks.models import Project, Todo
from mainapp.models import BaseUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = BaseUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    all_projects = graphene.List(ProjectType)
    related_users = graphene.List(UserType, projectName=graphene.String(required=True))

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_related_users(self, info, projectName):
        users = BaseUser.objects.all()
        projects = Project.objects.get(name=projectName)
        print(projects.user)
        try:
            return users.filter(uuid=projects.user.uuid)
        except Project.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
