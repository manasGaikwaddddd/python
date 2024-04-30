# class user:
#     def __init__(self,user_id,username,phone):
#         self.no=phone
#         self.id= user_id
#         self.username=username
#         self.follower=0
#         self.following=0
#     def follow(self,user):
#         user.follower +=1
#         self.following +=1
# user_1=user("1","manas","123")
# user_2=user("2","manas","1234")
# user_1.follow(user_2)
# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)


class manas:
    def __init__(self,myname,mydata):
        self.name=myname
        self.data=mydata
        self.follwer=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1
manas2=manas("1","MANAS")
manas3=manas("2","manas")
manas3.follow(manas2)



user4=manas("manas","pen")
print(user4.name)