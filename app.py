from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Senai'

login_manager = LoginManager(app)
#qual rota vai autenticar o login
login_manager.login_view = 'login'
login_manager.login_message = 'Para visualizar esta página realize o Login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado




@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/funcionarios')
@login_required
def funcionarios():
    func_sql = select(Funcionario)
    resultado = db_session.execute(func_sql).scalars().all()
    return render_template("funcionarios.html", resultado=resultado)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #pega o campo do formulario
        email = request.form['form-email']
        senha = request.form['form-senha']

        '''
        if not email or not senha:
            flash('Preencher todos os campos!', 'danger')
            return render_template('login.html')
            '''

        if not email or not senha:
            flash('Preencher todos os campos!', 'alert-danger')
            return render_template('login.html')

        else:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()

            if resultado_email:
                # se encontrado na base de dados
                if resultado_email.check_password(senha):

                    # realiza a autenticação:
                    login_user(resultado_email)

                    flash(f'Logado com sucesso!', 'success')
                    return redirect(url_for('home'))
                else:
                    # login incorreto
                    flash(f'Senha incorreta!', 'danger')
                    return render_template('login.html')

            else:
                flash(f'Email incorreto!', 'alert-danger')
                #redirect regarrega
                return redirect('login.html')


    return render_template('login.html')



@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/cadastro_funcionario', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        data_nascimento = request.form.get('from-date')
        cpf = request.form.get('form-cpf')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = float(request.form.get('form-salario'))
        print(f'{data_nascimento}')

        if not nome or not email or not senha:
            flash('Preencher todos os campos!', 'danger')
            return render_template('funcionarios.html')
        verifica_email = select(Funcionario).where(Funcionario.email == email)
        existe_email = db_session.execute(verifica_email).scalar_one_or_none()

        if existe_email:
            flash(f'Email {email} já esta cadastrado!', 'danger')
            return render_template('funcionarios.html')

        try:
            novo_funcionario = Funcionario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, email=email, senha=senha, cargo=cargo, salario=salario)
            novo_funcionario.set_password(senha)
            db_session.add(novo_funcionario)
            db_session.commit()
            flash(f'Funcionario {nome} cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))

        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar funcionario:', 'danger')
            print(f'Erro na base de dados{e}')
            return redirect(url_for('cadastro_funcionario'))

        except Exception as e:
            flash(f'Erro ao cadastrar funcionario:', 'danger')
            print(f'Erro na base de dados{e}')
            return redirect(url_for('cadastro_funcionario'))
    return render_template('funcionarios.html')


@app.route('/Geometria')
def Geometria():
    return render_template("geometria.html")


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            soma = n1 + n2
            flash("Soma realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # Passo 1: emitir a msg e a categoria do flash
            flash("preencher o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/subtracao', methods=['GET', 'POST'])
def subtracao():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            subtracao = n1 - n2
            flash("Subtração realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)
        else:
            flash("preencher o campo para realizar a subtracao", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            multiplicacao = n1 * n2
            flash("Multiplicação realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)
        else:
            flash("preencher o campo para realizar a multiplicação", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            divisao = n1 / n2
            flash("Divisão realizada", 'alert-success')

            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)
        else:
            flash("preencher o campo para realizar a divisão", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/Triangulo', methods=['GET', 'POST'])
def Triangulo():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Triangulo_area = n1 * n2 / 2
            flash("Divisão realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, Triangulo_area=Triangulo_area)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/Circulo', methods=['GET', 'POST'])
def Circulo():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Circulo_area = 3.14 * (n1 * n1)
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, Circulo_area=Circulo_area)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/Quadrado', methods=['GET', 'POST'])
def Quadrado():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Quadrado_area = n1 * n2
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n1, Quadrado_area=Quadrado_area)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/Hexagono', methods=['GET', 'POST'])
def Hexagono():
    if request.method == 'POST':
        if request.form['form_n1'] and request.form['form_n2']:
            n1 = int(request.form['form_n1'])
            n2 = int(request.form['form_n2'])
            Hexagono_area = n1 * n1 / 2 * 6
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, Hexagono_area=Hexagono_area)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/perimetro_triangulo', methods=['GET', 'POST'])
def perimetro_triangulo():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            triangulo_perimetro = n1 * 3
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, triangulo_perimetro=triangulo_perimetro)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/perimetro_circulo', methods=['GET', 'POST'])
def perimetro_circulo():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            circulo_perimetro = n1 * 2 * 3.14
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, circulo_perimetro=circulo_perimetro)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/perimetro_quadrado', methods=['GET', 'POST'])
def perimetro_quadrado():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            quadrado_perimetro = n1 * 4
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, quadrado_perimetro=quadrado_perimetro)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


@app.route('/perimetro_hexagonop', methods=['GET', 'POST'])
def perimetro_hexagonop():
    if request.method == 'POST':
        if request.form['form_n1']:
            n1 = int(request.form['form_n1'])
            hexagono_perimetro = n1 * 6
            flash("Conta realizada", 'alert-success')
            return render_template("geometria.html", n1=n1, hexagono_perimetro=hexagono_perimetro)
        else:
            flash("preencher o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")


# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)
