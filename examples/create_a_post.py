from linkedin_


user = User()
res = user.create_post(
    "test from my custom python APIs with two images",
    images=[
        ("/home/zuppif/Documents/LinkedInGPT/grogu.jpg", "grogu"),
        ("/home/zuppif/Documents/LinkedInGPT/grogu_2.png", "grogu2"),
    ],
)
