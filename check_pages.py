import subprocess

ps_script = """
try {
    $w = New-Object -ComObject Word.Application
    $w.Visible = $false
    $d = $w.Documents.Open('C:\\Users\\ammyp\\OneDrive\\Desktop\\DisasterConnectAI\\DisasterConnectAI_Project_Report.docx')
    $p = $d.ComputeStatistics(2)
    Write-Host "EXACT_PAGES: $p"
    $d.Close([ref]$false)
    $w.Quit()
} catch {
    Write-Host "ERR: $_"
}
"""

with open("test_pages.ps1", "w", encoding="utf-8") as f:
    f.write(ps_script)

res = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "test_pages.ps1"], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
