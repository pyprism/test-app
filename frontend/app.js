var baseUrl= 'http://127.0.0.1:8000/api/v1/todo/';

angular.module('todo', ['ngRoute'])
    .config(function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl : 'partials/home.html',
                controller : 'home'
            })
            .when('/todo', {
               templateUrl : 'partials/todo.html',
               controller : 'todo'
            })
            .when('/todo/:id', {
                templateUrl: 'partials/todoContent.html',
                controller : 'todoContent'
            });
    })
    .filter('isEmpty', function () {
        var bar;
        return function (obj) {
            for (bar in obj) {
                if (obj.hasOwnProperty(bar)) {
                    return false;
                }
            }
            return true;
        };
    })
    .controller('home', function($scope, request){
        request.get('http://127.0.0.1:8000/api/v1/notify/').then(function(data){
            $scope.list = data;
        });

    })
    .controller('todo', function($scope, request, $location){
        request.get(baseUrl).then(function(data){
            $scope.list = data;
            $scope.click = function(id){
                console.log(id);
                $location.path('/todo/' + id);
            }
        });
    })
    .controller('todoContent', function($scope, request, $routeParams){
        request.get(baseUrl + $routeParams.id).then(function(contents){
            $scope.title = contents.data.title;
            $scope.content = contents.data.content;
            $scope.date = contents.data.notify;
        });
        $scope.delete = function(){
            request.del( baseUrl + $routeParams.id + "/")
        };
        $scope.update = function(){
            var data = {
                title : $scope.title,
                content : $scope.content,
                notify : $scope.date,
                id : $routeParams.id
            };
            request.put(baseUrl+ $routeParams.id + '/', data);
        };
    })
    .factory('request', function($http, $location){
        var get = function(url){
           return $http.get(url).success(function(data){
               //console.log(data);
                return data;
            })
            .error(function(data,status){
                    console.log(data,status);
            });
        };
       var put = function(url , data){
           $http.put(url, data);
           $location.path('/todo');
       };
       var del = function(url){
           $http.delete(url);
           $location.path('/todo');
        };
       return {
            get : get,
            put : put,
            del : del
        };
    });