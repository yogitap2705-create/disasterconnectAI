
try {
    $w = New-Object -ComObject Word.Application
    $w.Visible = $false
    $d = $w.Documents.Open('C:\Users\ammyp\OneDrive\Desktop\DisasterConnectAI\DisasterConnectAI_Project_Report.docx')
    $p = $d.ComputeStatistics(2)
    Write-Host "EXACT_PAGES: $p"
    $d.Close([ref]$false)
    $w.Quit()
} catch {
    Write-Host "ERR: $_"
}
