<?php

/** @var \Laravel\Lumen\Routing\Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router->get('/hello', function () {
    print "Hello";
});

$router->get('/films', 'FilmController@get');
$router->get('/films/{id}', 'FilmController@getOne');
$router->post('/films', 'FilmController@post');
$router->put('/films/{id}', 'FilmController@put');
$router->delete('/films/{id}', 'FilmController@delete');

$router->get('/directors/{id}/films', 'DirectorController@getFilms');

$router->post('/rpc/validateAddress', 'AddressController@validateAddress');
$router->post('/rpc/sayHello', 'SayHelloController@hello');
