import json
import os 

class Contatos:
    def __init__(self, id, nome, telefone, email, endereco):
        self.id = id
        self.nome = nome
        self.telefone= telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome}\n Telefone: {self.telefone} | Email: {self.email}\n Endereço: {self.endereco}"
    
    def to_dict(self): 
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "endereço": self.endereco
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            telefone=data['telefone'],
            email=data.get('email'), 
            endereco=data.get('endereço')
        )

class Agenda:
    def __init__(self): 
        self._contatos = []
        self._arquivo = "arquivo.json"
        self.carregar_contatos()

    def _proximo_id(self):
        if not self._contatos:
            return 1
        else:
            return max(contato.id for contato in self._contatos) + 1

    def carregar_contatos(self):
        if os.path.exists(self._arquivo):
            with open(self._arquivo, 'r') as file: 
                dados = json.load(file)
            for contato_dict in dados:
                contato = Contatos.from_dict(contato_dict)
                self._contatos.append(contato)

    def salvar_contatos(self): 
        lista_dict_convertida = [contato.to_dict() for contato in self._contatos]
        with open(self._arquivo, 'w') as file:
            json.dump(lista_dict_convertida, file, indent=4)

    def adicionar_contato(self, contato):
        self._contatos.append(contato)
        self.salvar_contatos()

    def listar_contatos(self):
        for contato in self._contatos:
            print(contato)


# Teste de Execução
agenda = Agenda()
print("--------------------------------------------------")
print(f"1. Contatos carregados ao iniciar: {len(agenda._contatos)}") 

id1 = agenda._proximo_id()
contato1 = Contatos(id1, "Alice Silva", "11987654321", "alice@email.com", "Rua A, 10")
agenda.adicionar_contato(contato1)

id2 = agenda._proximo_id()
contato2 = Contatos(id2, "Bob Santos", "11912345678", "bob@email.com", "Av. B, 20")
agenda.adicionar_contato(contato2)

print(f"2. Novo ID gerado para Alice: {id1}")
print(f"3. Novo ID gerado para Bob: {id2}")
print(f"4. Contatos após adição: {len(agenda._contatos)}") 

print("\n--- 5. Lista de Contatos ---")
agenda.listar_contatos() 

print("\n--- 6. Teste de Recarregamento ---")
nova_agenda = Agenda()
print(f"7. Contatos carregados na nova instância: {len(nova_agenda._contatos)}")