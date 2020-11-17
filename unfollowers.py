 

followers = open("/Users/neeltangella/Desktop/following.txt", "r")
following = open("/Users/neeltangella/Desktop/followers.txt", "r")


followers = followers.read()
following = following.read()


followers = followers.split()
following = following.split()

def unfollower_finder(following, followers): 
    aa = []
    
    
    for user in followers: 
        if user not in following: 
            aa.append(user)
    
    
    return aa 

print(unfollower_finder(following, followers))