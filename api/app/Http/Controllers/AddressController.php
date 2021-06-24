<?php

namespace App\Http\Controllers;

use Illuminate\Http\Response;
use Illuminate\Http\Request;
use Illuminate\Validation\ValidationException;

class AddressController extends Controller
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
    public function validateAddress(Request $request)
    {
        try {
            $this->validate($request, [
                'field_1' => 'required|string',
                'field_2' => 'string',
                'city' => 'required|string',
                'postcode' => 'required|string|regex:/[A-PR-UWYZa-pr-uwyz]{1,2}[0-9][0-9A-HJKPS-UWa-hjkps-uw]? ?[0-9][ABD-HJLNP-UW-Zabd-hjlnp-uw-z]{2}/i'
            ]);

            return new Response('', 200);
        } catch (ValidationException $e) {
            return new Response($e->getMessage(), 400);
        }
    }
}
