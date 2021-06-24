<?php

namespace App\Http\Controllers;

use Illuminate\Http\Response;
use Illuminate\Http\Request;
use Illuminate\Validation\ValidationException;

class SayHelloController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
    }

    /**
     * POST endpoint: return film by ID.
     *
     * @param int $id ID of the film record to retrieve.
     * @return string JSON response.
     */
    public function hello(Request $request)
    {
        return $request->json('name') ? new Response('Hello, ' . $request->json('name'), 200) : new Response('Name not specified.', 400);
    }
}
