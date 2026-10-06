from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


puzzles = {
    4: [
        {
            "puzzle": [
                [1, 0, 0, 4],
                [0, 4, 1, 0],
                [0, 1, 4, 0],
                [4, 0, 0, 1]
            ],
            "solution": [
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                [2, 1, 4, 3],
                [4, 3, 2, 1]
            ]
        },
        {
            "puzzle": [
                [0, 2, 3, 0],
                [3, 0, 0, 2],
                [0, 1, 4, 0],
                [4, 0, 0, 1]
            ],
            "solution": [
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                [2, 1, 4, 3],
                [4, 3, 2, 1]
            ]
        }
    ],

    6: [
        {
            "puzzle": [
                [1, 0, 3, 0, 5, 0],
                [0, 5, 0, 1, 0, 3],
                [2, 0, 4, 0, 6, 0],
                [0, 6, 0, 2, 0, 4],
                [3, 0, 5, 0, 1, 0],
                [0, 4, 0, 6, 0, 2]
            ],
            "solution": [
                [1, 2, 3, 4, 5, 6],
                [4, 5, 6, 1, 2, 3],
                [2, 3, 4, 5, 6, 1],
                [5, 6, 1, 2, 3, 4],
                [3, 4, 5, 6, 1, 2],
                [6, 1, 2, 3, 4, 5]
            ]
        }
    ],

    9: [
        {
            "puzzle": [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ],
            "solution": [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ]
        }
    ]
}


def get_random_puzzle(size):
    return random.choice(puzzles[size])


@app.route("/")
def index():

    size = int(request.args.get("size", 9))
    round_number = int(request.args.get("round", 1))

    if size not in puzzles:
        size = 9

    puzzle = get_random_puzzle(size)

    return render_template(
        "index.html",
        size=size,
        round_number=round_number,
        puzzle=puzzle["puzzle"],
        solution=puzzle["solution"]
    )


@app.route("/new_round")
def new_round():

    size = int(request.args.get("size", 9))
    round_number = int(request.args.get("round", 1))

    if size not in puzzles:
        size = 9

    round_number += 1

    puzzle = get_random_puzzle(size)

    return jsonify({
        "size": size,
        "round": round_number,
        "puzzle": puzzle["puzzle"],
        "solution": puzzle["solution"]
    })


@app.route("/verify_hint_code", methods=["POST"])
def verify_hint_code():

    data = request.get_json()

    if not data:
        return jsonify({
            "correct": False
        })

    code = data.get("code", "")

    if code == "doydoygwapo":
        return jsonify({
            "correct": True
        })

    return jsonify({
        "correct": False
    })

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    import os

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )