def travels(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    #user_trips = Trip.objects.filter(trip_creator=user.id)
    other_trips = Trip.objects.exclude(trip_creator=user.id)
    context = {
        'user': user,
        "user_trips": user_trips,
        
    context = {
        'wall_messages': Wall_Message.objects.all()
    }
    }
    return render(request, 'travels.html', context)


     <h3> View Trip</h3>
    <p>Destination {{ trip.destination}}</p>
    <p>Creator name:{{ trip.trip_creator.first_name }}</p>
    <p>{{ trip.trip_creator.last_name }}</p>
    <p>Trip Description {{ trip.description }}</p>
    <p>Start date{{ trip.start_date|date:"SHORT_DATE_FORMAT" }}</p>
    <p>end date{{ trip.end_date|date:"SHORT_DATE_FORMAT" }}</p>
    

    <h4>Other Users Joing the Trip</h4>