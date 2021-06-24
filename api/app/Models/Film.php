<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Film extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'title',
        'release_year',
        'description',
        'rating'
    ];

    protected $table = 'film';

    public $timestamps = false;
}
