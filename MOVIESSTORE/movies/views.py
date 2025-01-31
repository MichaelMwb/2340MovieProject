from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from .models import Movie, Review 
=======
from .models import Movie, Review
>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
from django.contrib.auth.decorators import login_required

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': template_data})
def show(request, id):
<<<<<<< HEAD
    movie =  Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
=======
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
<<<<<<< HEAD
    return render(request, 'movies/show.html',
        {'template_data': template_data})
=======
    return render(request, 'movies/show.html', {'template_data': template_data})

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
<<<<<<< HEAD
=======

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show', id=id)
<<<<<<< HEAD
=======

>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
<<<<<<< HEAD
        return render(request, 'movies/edit_review.html',
            {'template_data': template_data})
=======
        return render(request, 'movies/edit_review.html', {'template_data': template_data})
>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
<<<<<<< HEAD
@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id,
        user=request.user)
=======

@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
>>>>>>> 34cdd02e7b63105c3685ae56cab15bcfcdf10102
    review.delete()
    return redirect('movies.show', id=id)