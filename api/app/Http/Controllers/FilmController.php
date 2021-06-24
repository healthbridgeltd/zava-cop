<?php

namespace App\Http\Controllers;

use App\Models\Film;
use Illuminate\Database\QueryException;
use Illuminate\Http\Response;
use Illuminate\Http\Request;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

class FilmController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }

    /**
     * GET endpoint: return film by ID.
     *
     * @param int $id ID of the film record to retrieve.
     * @return string JSON response.
     */
    public function get(int $id)
    {
        try {
            $film = Film::findOrFail($id);
            return new Response(['data' => $film], 200);           
        } catch (NotFoundHttpException $e) {
            return new Response(['error' => $e->getMessage()], 404);
        }
    }

    /**
     * POST endpoint: create record with data.
     *
     * @return string JSON response.
     */
    public function post(Request $request)
    {
        $this->validate($request, [
            'title' => 'required',
            'release_year' => 'required|integer',
            'director_id' => 'required'
        ]);

        try {
            $film = Film::create($request->all());
            return new Response(['data' => $film, 200]);    
        } catch (QueryException $e) {
            return new Response(['error' => $e->getMessage()], 400);
        }
    }
}
