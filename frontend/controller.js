angular.module('todo', ['ngRoute'])
.config(function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl : 'partials/home.html'
            });
    });