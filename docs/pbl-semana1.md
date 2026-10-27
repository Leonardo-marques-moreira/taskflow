1. Diagnóstico dos problemas

1. Código trocado por pendrive, e-mail e ZIP: Sharing (Compartilhamento).
Cada pessoa trabalha na própria cópia, não existe histórico central e ninguém sabe quem mudou o quê. Conhecimento e responsabilidade não são compartilhados.

2. Bruno sobrescreveu a tela de cupons da Carla: Lean.
O trabalho não flui em lotes pequenos e integrados. Os arquivos são copiados por cima uns dos outros, sem revisão, e a correção do frete levou junto a tela de cupons da Carla.	

3. Ninguém sabe qual versão está em produção: Measurement (Medição).
Sem registro do que foi publicado, a equipe não tem dados para investigar as reclamações dos clientes nem saber o que mudou no ar.

4. Deploy manual por FTP, feito só pela Ana: Automation (Automação).
Tarefa repetitiva feita à mão, por uma única pessoa, sujeita a erro humano.

2. Fluxo mínimo com Git e GitHub

Clonar: cada desenvolvedor utiliza `git clone` para obter uma cópia local do repositório no GitHub.
Criar uma branch: cada tarefa é desenvolvida em uma branch própria, por exemplo, `feature/cupons`, sem alterar diretamente a branch principal.
Registrar as mudanças: após modificar e testar o código, o desenvolvedor utiliza `git add` e `git commit`, com uma mensagem clara sobre as alterações.
Enviar e revisar: utiliza `git push` para enviar a branch ao GitHub e abre um Pull Request para revisão por outro desenvolvedor.
Integrar e testar: após a aprovação, as alterações são integradas à branch `main` e os testes são executados.
Atualizar a produção: a versão aprovada é publicada no servidor e a aplicação é verificada após a atualização.

3. Recuperação da tela de cupons da Carla

Se a tela de cupons foi registrada em um commit, ela estará disponível no histórico do repositório. Para recuperá-la, a equipe deve:

1. Localizar o commit em que a tela estava correta usando `git log -- caminho/da/tela-de-cupons`.
2. Restaurar o arquivo daquela versão usando `git restore --source=<hash-do-commit> -- caminho/da/tela-de-cupons`.
3. Testar a recuperação e registrá-la em um novo commit.

O processo pode levar poucos minutos, sem precisar reconstruir a tela do zero. Isso depende de a versão correta ter sido registrada no Git. O caminho do arquivo e o hash 
devem ser substituídos pelos valores reais do projeto.

4. Risco que o Git sozinho não resolve

Deploy manual por FTP:  o Git controla o histórico do código, mas não garante que os arquivos sejam publicados corretamente no servidor. Mesmo com o repositório organizado, Ana pode copiar arquivos errados, esquecer algum arquivo ou publicar uma versão incompleta. Como a publicação é manual, a equipe deve testar a versão antes do deploy e verificar o funcionamento da aplicação após a atualização.

A automação do deploy pode reduzir esses riscos, tornando a publicação mais consistente e menos dependente da atenção de uma única pessoa.