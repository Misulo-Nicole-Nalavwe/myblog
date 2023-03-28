from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blogappposts.models import Category, Post

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    
class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
    def lastmoddate(self, obj):
        return obj.created_at

