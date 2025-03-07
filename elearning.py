import streamlit as st
import random

def autenticar_usuario():
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Login"):
        if usuario == "admin" and senha == "1234":
            st.session_state['autenticado'] = True
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha inválidos")

def sincronizar_dados():
    st.write("Sincronizando dados com o LMS...")
    st.success("Dados sincronizados com sucesso!")

def exportar_dados():
    st.write("Exportando dados dos alunos...")
    st.success("Dados exportados com sucesso!")

def main():
    st.title("📚 E-Learning com python")
    
    if 'autenticado' not in st.session_state:
        st.session_state['autenticado'] = False
    
    if not st.session_state['autenticado']:
        autenticar_usuario()
        return
    
    menu = ["Início", "Cursos", "Quiz", "Gestão de Usuários", "Relatórios"]
    choice = st.sidebar.selectbox("Navegação", menu)
    
    if choice == "Início":
        st.subheader("Bem-vindo a nossa plataforma de aprendizado!")
        st.write("Escolha um curso na aba lateral e comece a aprender!")
    
    elif choice == "Cursos":
        curso = st.selectbox("Escolha um curso:", ["Python Básico", "Machine Learning", "Banco de Dados"])
        
        if curso == "Python Básico":
            st.video("https://youtu.be/kqtD5dpn9C8?si=icD44X8q9ySUewEv")
        elif curso == "Machine Learning":
            st.video("https://youtu.be/ukzFI9rgwfU?si=P-HHtcEBB5REvg3x")
        elif curso == "Banco de Dados":
            st.video("https://youtu.be/HXV3zeQKqGY?si=tbfVZmsJh50KZ4Ce")
    
    elif choice == "Quiz":
        st.subheader("Teste seus conhecimentos!")
        perguntas = {
            "O que significa a sigla SQL?": ["Structured Query Language", "Simple Query Language", "System Query Logic", "None of the above"],
            "Qual biblioteca é mais usada para Machine Learning em Python?": ["Pandas", "Matplotlib", "Scikit-Learn", "Requests"],
            "Qual desses é um tipo de banco de dados NoSQL?": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"]
        }
        
        score = 0
        for pergunta, opcoes in perguntas.items():
            resposta = st.radio(pergunta, opcoes)
            if resposta == opcoes[0]:
                score += 1
        
        if st.button("Finalizar Quiz"):
            st.success(f"Você acertou {score} de {len(perguntas)} perguntas!")
            st.balloons()
    
    elif choice == "Gestão de Usuários":
        st.subheader("Gerenciamento de Usuários")
        opcao = st.radio("Escolha uma ação", ["Criar Usuário", "Editar Usuário", "Excluir Usuário"])
        if opcao == "Criar Usuário":
            st.text_input("Nome do Usuário")
            st.text_input("E-mail")
            st.button("Criar")
        elif opcao == "Editar Usuário":
            st.selectbox("Selecione o usuário", ["user1", "user2", "user3"])
            st.button("Editar")
        elif opcao == "Excluir Usuário":
            st.selectbox("Selecione o usuário", ["user1", "user2", "user3"])
            st.button("Excluir")
    
    elif choice == "Relatórios":
        st.subheader("Relatórios de Progresso")
        st.write("Visualização de estatísticas de desempenho.")
        sincronizar_dados()
        exportar_dados()
    
if __name__ == "__main__":
    main()
