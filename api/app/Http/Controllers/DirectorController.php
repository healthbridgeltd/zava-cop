<?php

namespace App\Http\Controllers;

use App\Models\Director;
use App\Models\Film;
use Illuminate\Database\QueryException;
use Illuminate\Http\Response;
use Illuminate\Http\Request;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

class DirectorController extends Controller
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

    public function getFilms(int $id)
    {
        $films = Film::where('director_id', '=', $id)->get();
        if (count($films)) {
            return new Response(['data' => $films], 200);
        }

        return new Response('No films found for that director.', 404);
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
            $director = Director::findOrFail($id);
            return new Response(['data' => $director], 200);           
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
            'name' => 'required|string',
        ]);

        try {
            $director = Director::create($request->all());
            return new Response(['data' => $director, 200]);    
        } catch (QueryException $e) {
            return new Response(['error' => $e->getMessage()], 400);
        }
    }
}
