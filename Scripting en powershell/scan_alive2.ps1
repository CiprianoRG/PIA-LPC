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
#Genramos un bucle for
Write-Output ""
Write-Host " -- Subred actual: "
Write-Host "Escaneando:" -NoNewline;Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
Write-Output ""
foreach ($r in $rango_ip)
{
    $actual = $rango+$r
    $responde = Test-Connection $actual -Quiet -Count 1
    if ($responde -eq "True")
    {
        Write-Output ""
        Write-Host "Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}
#fin