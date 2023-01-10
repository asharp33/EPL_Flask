from flask import Flask, request, render_template

app = Flask(__name__)

class EplResults:
    def __init__(self, year, team, rank, mp, won, draw, lost, gf, ga, gd, pts, notes):
        self.year = year
        self.team = team
        self.rank = rank
        self.mp = mp
        self.won = won
        self.draw = draw
        self.lost = lost
        self.gf = gf
        self.ga = ga
        self.gd = gd
        self.pts = pts
        self.notes = notes

def get_results_for_year(season):
    results = []
    for result in allresults:
        if result.rank == season:
            results.append(result)
    return results

@app.route('/results')
def show_results():
    season = request.args.get('season')
    if season is None:
        season = '1'
    results = get_results_for_year(season)
    sorted_results = sorted(results, key=lambda x: x.year, reverse=True)  # sort the results by rank
    return render_template('results.html', results=sorted_results)

if __name__ == '__main__':
    with open("epl_league_tables.csv") as f:
        data = f.readlines()
    allresults = []
    for line in data:
        values = line.strip().split(",")
        year = values[0]
        team = values[1]
        rank = values[2]
        mp = values[3]
        won = values[4]
        draw = values[5]
        lost = values[6]
        gf = values[7]
        ga = values[8]
        gd = values[9]
        pts = values[10]
        notes = values[11]
        results = EplResults(year, team, rank, mp, won, draw, lost, gf, ga, gd, pts, notes)
        allresults.append(results)
    app.run()
