$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu gateway..."
Write-Host "Tu gateway: $subred"
#Determinando rango de subred
$rango = $subred.substring(0,$subred.Indexof('.')+1+$subred.substring($subred.Indexof('.')+1).indexof('.')+3)
Write-Host "== Determinando tu rango de subred..."
echo $rango
#Determinando si rango termina en .
$punto = $rango.EndsWith('.')
if ($punto -like "False")
{
    $rango= $rango+'.'
}
#
$rango_ip = @(1..254)
# Definimos un array con puertos a escanear
$portstoscan = @(20, 21, 22, 23, 50, 51, 53, 80, 110, 119, 135, 143, 145, 151, 443, 445, 137, 138, 139, 3306, 1521, 27017, 27018, 5432, 8080)
$waittime=100

#Solicitamos direccion a escanear
Write-Host "Direccion ip a escanear: " -NoNewline
$direccion= Read-Host
#generamos un bucle for
foreach ($p in $portstoscan)
{
    $TCPobject = New-Object System.Net.Sockets.TcpClient
        try{$resultado = $TCPobject.ConnectAsync($direccion,$p).Wait($waittime)} catch{}
        if ($resultado -eq "True")
        {
            Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
        }
}