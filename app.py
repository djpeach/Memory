from bottle import route, run, template, static_file, get, post, request
from Tile import tiles
from random import shuffle
import time

faceUpTileCount = 0
previousTile = None
matched = 0
start_time = None

@route('/static/index.html')
def server_static(filename):
    return static_file(filename, root="./static")


@get('/')
def index():
    return template('index.html', allTiles=tiles, matched=0)


@get('/clickedTile')
def clickedTile():
    global faceUpTileCount, previousTile, matched, start_time

    if not start_time:
        start_time = time.time()

    if (faceUpTileCount >= 2):
        faceUpTileCount = 0
        previousTile = None
        for card in [card for card in tiles if not card.matched]:
            card.backgroundColor = "black"

    index = request.query.selectedButton
    index = int(index)
    currentTile = tiles[index]

    if(previousTile and previousTile.color == currentTile.color and previousTile != currentTile):
        previousTile.backgroundColor = "transparent"
        currentTile.backgroundColor = "transparent"
        previousTile.matched = True
        currentTile.matched = True
        faceUpTileCount = 0
        matched += 1
    elif (not currentTile.matched and previousTile != currentTile):
        currentTile.backgroundColor = currentTile.color
        currentTile.score = currentTile.score - 1 if currentTile.score > 0 else 0
        faceUpTileCount += 1
        previousTile = currentTile

    unmatchedTiles = [tile for tile in tiles if not tile.matched]

    if len(unmatchedTiles) == 0:
        end_time = time.time()
        elapsed_time = end_time - start_time
        bonus_time = max(60 - elapsed_time, 0)
        bonus_score = int(bonus_time * .45)
        score = 0
        for tile in tiles:
            score = score + tile.score if tile.score <= 10 else score +  10
        score *= 3
        score += bonus_score
        score = f"{score} / {len(tiles) * 10 * 3 + (int(60 * .45))}"
        return template('winner.html', score=score)
    else:
        return template('index.html', allTiles=tiles, matched=matched)

@get('/reset')
def reset():

    global matched, previousTile, faceUpTileCount

    matched = 0
    previousTile = None
    faceUpTileCount = 0

    for tile in tiles:
        tile.matched = False
        tile.backgroundColor = "black"
        tile.score = 11

    shuffle(tiles)

    return template('index.html', allTiles=tiles, matched=matched)



run(host='localhost', port=8080, debug=True, reloader=True)
