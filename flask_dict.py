from flask import Flask
from flask import render_template, request
import pickle

app = Flask(__name__)


class Entry:
    
    def __init__(self, lex):
        self.lex = lex
        
        self.pos = {}
        self.sem = {}
        self.gramm = {}
        self.examples = defaultdict(list)
        
    def add_pos(self, pos):
        if pos not in self.pos:
            self.pos[pos] = {}
    
    def add_sem(self, pos, sem):
        if sem not in self.pos[pos]:
            self.pos[pos][sem] = {}
    
    def add_form(self, pos, sem, gramm, form):
        if gramm not in self.pos[pos][sem]:
            self.pos[pos][sem][gramm] = form
            
    def add_example(self, sem, doc, pair):
        self.examples[sem].append((doc, pair))
            
    def get_tree(self):
        return self.pos

class Pair:
    
    def __init__(self, id_, bua, rus):
        self.id_ = id_
        self.tokens_bua, self.infos_bua = bua
        self.tokens_rus, self.infos_rus = rus
        
        self.text_bua = ''.join(self.tokens_bua).strip()
        self.text_rus = ''.join(self.tokens_rus).strip()
        
    def find_rus_in_bua(self, word):
        res = []
        
        for token, info in zip(self.tokens_bua, self.infos_bua):
            _info = info.get('sem')
            
            if _info is not None and word in _info:
                res.append((word, token, info))
                
        return res


with open('bua_data.pickle', 'rb') as f:
    bua_data = pickle.load(f)

with open('bua_rus_entries.pkl', 'rb') as f:
    rus_data = pickle.load(f)

with open('rus_rus.pkl', 'rb') as f:
    rus_rus = pickle.load(f)


@app.route('/', methods=['GET'])
def rus():

    global bua_data

    if request.args:
        query1 = request.args['query1']

        result = bua_data.get(query1)
        
        if result:
            res = result.get_tree()
            sns = result.examples
        
            return render_template('answer_bua.html', res=res, word=query1, sns=sns)

    return render_template('bua.html')


@app.route('/rus', methods=['GET'])
def bua():

    if request.args:
        query1 = request.args['query1']

        r_quer = rus_rus.get(query1)

        if r_quer:
            result = []
            for q in r_quer:
                if rus_data.get(q):
                    result.append(rus_data.get(q))

            return render_template('answer_rus.html', res=result, word=query1)

    return render_template('bua.html')


if __name__ == '__main__':
    app.run(debug=True)
