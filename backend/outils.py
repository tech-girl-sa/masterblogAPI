from data.data import POSTS


def sort_posts(sort, direction):
    sorted_posts = POSTS
    if sort == "title":
        sorted_posts = sorted(sorted_posts, key=lambda x: x["title"].lower())
        if direction == "desc":
            sorted_posts = sorted(sorted_posts, key=lambda x: x["title"].lower(), reverse=True)
    if sort == "content":
        sorted_posts = sorted(sorted_posts, key=lambda x: x["content"].lower())
        if direction == "desc":
            sorted_posts = sorted(sorted_posts, key=lambda x: x["content"].lower(), reverse=True)
    return sorted_posts


def fetch_post_by_id(id):
    posts = [post for post in POSTS if post['id']==id]
    if len(posts) > 0:
        return posts[0]