# MediaFileMover
MediaFileMover é uma classe que move arquivos de uma pasta para outra, organizando-os por data.

# Características
<br>
Move arquivos de uma pasta para outra organizando-os por data.
O arquivo é movido para uma pasta com o nome do mês (localizado em português - pt_BR) e uma pasta com o dia da data.
Caso uma pasta esteja vazia, ela é removida.
O processo de movimentação de arquivos é repetido a cada 30 segundos.
Utilização
Instancie a classe MediaFileMover informando o caminho da pasta de origem e o caminho da pasta de destino.

<br>
<br>

[```mover = MediaFileMover('C:/Users/Administrador/Desktop/teste Delivery', 'C:/Users/Administrador/Desktop/teste delivery destino')```]

Execute o método move_files() para iniciar a movimentação de arquivos.

<br>
<br>

[```mover.move_files()```]

<br>
<br>

Para que a movimentação de arquivos seja repetida a cada 30 segundos, utilize um loop.

<br>
<br>

```while True:
    mover.move_files()
    sleep(30)```

<br>
<br>

# Observações

<br>

É importante observar que os arquivos devem estar armazenados em pastas que contenham a data de criação no formato ddMMYY no final do nome da pasta. Exemplo: "pasta_102220"
Esse script move arquivos para a pasta de destino e delete pasta vazia e arquivo que esta dentro da pasta, então esteja atento ao utilizar.

# Dependências

<br>
<br>

os
re
logging
datetime
shutil
time
babel.dates
Logging

<br>
<br>

As informações de log são registradas com o nível de informação (INFO).
As mensagens de log são no formato: %(asctime)s [%(levelname)s]: %(message)s, data e hora do log é no formato: %Y-%m-%dT%H:%M:%S.%fZ.
Exemplo

[```2021-12-29T19:10:12.401Z [INFO]: Successfully moved example.jpg to >> C:/Users/Administrador/Desktop/teste delivery destino/DEZEMBRO/29/pasta_292220```]

<br>
<br>

# Como funciona

<br>

A classe MediaFileMover tem dois atributos, src_dir e dst_dir, que representam respectivamente o caminho da pasta de origem e o caminho da pasta de destino. Ao instanciar a classe, esses atributos são inicializados com os valores passados como parâmetros.

O método move_files() é responsável por percorrer todos os arquivos dentro da pasta de origem e, caso encontre algum arquivo dentro de uma pasta com nome terminado em data no formato ddMMYY (por exemplo, "pasta_292220"), ele move o arquivo para a pasta de destino organizado por mês e dia. O mês é o nome localizado em português e o dia é obtido a partir da data extraída do nome da pasta. Caso a pasta de destino ainda não exista, ela é criada.

Além disso, o método move_files() também remove as pastas vazias dentro da pasta de origem. Isso é feito percorrendo as pastas dentro da pasta de origem e verificando se elas estão vazias, caso sim, ela é removida.

# Use Case

<br>

Este script é útil em casos onde é necessário manter arquivos organizados por data e automaticamente movê-los para sua pasta de destino. Por exemplo, se você tiver uma pasta com imagens tiradas por uma câmera e quiser organizá-las por data, você pode usar este script para fazer isso automaticamente. Além disso, se você estiver trabalhando com fluxo de arquivos em um pipeline automatizado, você pode usar este script para organizar os arquivos de acordo com a data em que foram criados.
Outra utilidade seria para casos onde é necessário manter arquivos organizados por data e automaticamente movê-los para outra pasta de armazenamento, tal como por exemplo organizar arquivos de relatórios, backups de arquivos, etc.
É importante notar que este script utiliza a biblioteca babel.dates para formatar o nome do mês em português, então é necessário instalá-lo antes de usar o script. Além disso, como o script está configurado para repetir a movimentação de arquivos a cada 30 segundos, é importante ter em mente o impacto desse processo em seu sistema, e talvez utilizar uma abordagem diferente caso seja necessário.

<br>
<br>

# Conclusão

<br>

MediaFileMover é uma classe simples mas poderosa que pode ajudar a manter seus arquivos organizados automaticamente. Com suas características de organização de arquivos por data e sua capacidade de remover pastas vazias, ele pode ser uma ferramenta valiosa em diversos cenários. É importante notar que o script modifica as pastas e arquivos em seu sistema, então é importante testá-lo antes de utilizá-lo em um ambiente de produção.
