import json

from rest_framework.test import APITestCase

from users.models        import User


class UserSignUpTest(APITestCase):
        
    def test_create_account_success(self):
        data = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['email'], 'testemail@gmail.com')
        
    def test_create_account_duplicate_email_fail(self):
        User.objects.create(
            id         = 1,
            email      = 'testemail@gmail.com',
            password   = 'testpassword12!',
            first_name = 'David',
            last_name  = 'kim'
        )
        
        data = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {"email" : ["user의 email은/는 이미 존재합니다."]})        
 
    def test_create_account_invalid_email_fail(self):
        data = {            
            'email'      : 'testemailgmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'email' : ['유효한 이메일 주소를 입력하십시오.']})

    def test_create_account_invalid_password_fail(self):
        data = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'message' : ['숫자와 영문자 조합 8자를 입력해주세요']})
    
    def test_create_account_field_missing_fail(self):
        data = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'first_name' : ['이 필드는 필수 항목입니다.']})
    
    
class UserSignInTest(APITestCase):
            
    def test_user_signin_success(self):
        user = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(user), content_type='application/json')
        
        data = {
            "email"    : "testemail@gmail.com",
            "password" : "testpassword12!"
        } 
        url = '/users/signin'
        
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_user_signin_invalid_email_fail(self):
        user = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(user), content_type='application/json')

        data = {
            "email"    : "testinvalidemailgmailcom",
            'password' : 'testpassword12!',
        } 
        url = '/users/signin'
        
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'email': ['유효한 이메일 주소를 입력하십시오.']})
        
    def test_user_signin_invalid_password_fail(self):
        user = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(user), content_type='application/json')

        data = {
            "email"    : "testemail@gmail.com",
            "password" : "testwrongpassword1234567890!"
        } 
        url = '/users/signin'
        
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'message': ['올바른 password를 입력해주세요']})
        
    def test_user_signin_account_does_not_exist_fail(self):
        user = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(user), content_type='application/json')

        data = {
            "email"    : "testwrongemail@gmail.com",
            'password' : 'testpassword12!',
        } 
        url = '/users/signin'
        
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'message': ['사용자가 존재하지 않습니다.']})

    def test_user_signin_field_missing_fail(self):
        user = {            
            'email'      : 'testemail@gmail.com',
            'password'   : 'testpassword12!',
            'first_name' : 'David',
            'last_name'  : 'kim'
        }
        url = '/users/signup'
        
        response = self.client.post(url, data=json.dumps(user), content_type='application/json')

        data = {
            "password" : "testpassword12!"
        } 
        url = '/users/signin'
        
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.json(), {'message': ['email 또는 password를 입력해주세요.']})