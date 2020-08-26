from knox.models import AuthToken
class Get_response():
    def Response_Data(self, usermodel, user_instance):
        data =  {"user":usermodel(
                user_instance, 
                context=self.get_serializer_context()).data, 
                 # The token Model is used to create authentication 
                 # token for each request
                "token":AuthToken.objects.create(user_instance)[1]         
          }
        return data