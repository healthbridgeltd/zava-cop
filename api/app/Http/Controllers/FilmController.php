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

    public function get(Request $request)
    {
        $films = Film::where($request->all())->get();
        if (count($films)) {
            return new Response(['data' => $films], 200);
        }

        return new Response('No films found.', 404);
    }

    /**
     * GET endpoint: return film by ID.
     *
     * @param int $id ID of the film record to retrieve.
     * @return string JSON response.
     */
    public function getOne(int $id)
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

    /**
     * PUT endpoint: update record with data.
     *
     * @return string JSON response.
     */
    public function put(Request $request, int $id)
    {
        try {
            $film = Film::findOrFail($id);
            $film->update($request->all());

            return new Response(['data' => $film], 200);    
        } catch (QueryException $e) {
            return new Response(['error' => $e->getMessage()], 400);
        }
    }

    /**
     * DELETE endpoint: delete record.
     *
     * @return string JSON response.
     */
    public function delete(int $id)
    {
        try {
            Film::findOrFail($id)->delete();

            return new Response('Deleted', 200);    
        } catch (QueryException $e) {
            return new Response(['error' => $e->getMessage()], 400);
        }
    }
}
