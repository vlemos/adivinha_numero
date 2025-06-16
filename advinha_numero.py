import streamlit as st
import time
import random


def fim_jogo(resultado, caminho_ranking='ranking.xls'):
    st.session_state.estado_jogo = 'sem_jogo'

    if resultado == "Vitoria":
        st.success(f'Você venceu! Parabéns! Sua pontuação foi de {st.session_state.tentativas} pontos')
    
        

    elif resultado == "Derrota":
        st.error(f'Você perdeu! Tente novamente. A resposta correta era {st.session_state.numero_secreto}' )
    
    # Reinicia o jogo
    #del st.session_state.numero_secreto
    #del st.session_state.numero_maximo
    #st.session_state.tentativas = 10
    #st.session_state.dificuldade = 'Iniciante'
    
    #st.rerun()

def jogando(dificuldade):




    # Inicialização dos estados

    if 'estado_jogo' not in st.session_state:
        st.session_state.estado_jogo = 'jogando'

    if 'tentativas' not in st.session_state:
        st.session_state.tentativas = 10

    if 'dificuldade' not in st.session_state:
        st.session_state.dificuldade = dificuldade 

    if 'numero_maximo' not in st.session_state:
        if st.session_state.dificuldade == 'Iniciante':
            st.session_state.numero_maximo = 100
        elif st.session_state.dificuldade == 'Intermediário':
            st.session_state.numero_maximo = 1000 
        elif st.session_state.dificuldade == 'Avançado':
            st.session_state.numero_maximo = 10000    

    if 'numero_secreto' not in st.session_state:
        st.session_state.numero_secreto = random.randint(1, st.session_state.numero_maximo)
    
 
        
        
    col1, col2 = st.columns([1,2])

    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.write(f'Tentativas restantes: {st.session_state.tentativas}')
        st.write(f' Seu Nível atual é: {st.session_state.dificuldade}')
        st.write(f' Número secreto: {st.session_state.numero_secreto}')
        #st.write(f' Número máximo: {st.session_state.numero_maximo}')
     
        
    with col2:
        st.write(f'Tente adivinhar o número que estou pensando entre 1 e {st.session_state.get("numero_maximo")}')
        palpite = st.number_input("Digite seu palpite:", min_value=1, max_value=st.session_state.numero_maximo, step=1)

        if st.session_state.estado_jogo == 'jogando':
            if st.session_state.tentativas > 0:
                if st.button("Chutar"):
                
               
              
                    if palpite == st.session_state.numero_secreto:
                        st.success("Parabéns! Você acertou o número!")
                        st.balloons()
                        time.sleep(2)
                        # Reinicia o jogo
                        del st.session_state.numero_secreto
                        del st.session_state.numero_maximo
                        st.session_state.tentativas = st.session_state.tentativas + 10
                        if st.session_state.dificuldade == "Iniciante":
                            st.session_state.dificuldade = "Intermediário"
                        elif st.session_state.dificuldade == "Intermediário":
                            st.session_state.dificuldade = "Avançado"
                        else:
                            fim_jogo("Vitoria")
                        st.rerun()

                    elif palpite < st.session_state.numero_secreto:
                        st.info("O número é maior.")


                    else :
                        st.info("O número é menor.")
                   

                
                    st.session_state.tentativas -= 1
                    time.sleep(1)
                    if st.session_state.tentativas == 0:
                        if st.session_state.estado_jogo == 'sem_jogo':
                            fim_jogo("Derrota")

                    st.rerun()
            else:
                
                fim_jogo("Derrota")

            st.caption("Criado por Vinicius Lemos de Souza")
    

st.title('Adivinha o Número!')

if not st.session_state.get('nome'):
    st.write('Olá! Bem-vindo ao jogo de adivinhação de números!')
    nome = st.text_input('Qual é o seu nome?', key='input_nome_temp')

    if st.button('Enviar Nome'):
        if nome.strip() != '':
            st.session_state.nome = nome
        if st.session_state.get('nome'):
            if st.session_state.get('nome') == nome:
                st.rerun()
else:
    st.write(f'Olá, {st.session_state.get("nome")}! Vamos jogar?!')
    st.write('')
    st.write('')
    jogando('Iniciante')
   






#st.write('Tente adivinhar o número que estou pensando entre 1 e 100!')  