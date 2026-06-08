# 本地安装 video-generation-skills 到 Cursor（开发用）
# Usage: .\scripts\install-local.ps1 [-Global]

param(
    [switch]$Global
)

$RepoRoot = Split-Path -Parent $PSScriptRoot
$SkillsArgs = @("add", $RepoRoot, "--all", "-a", "cursor", "-y")

if ($Global) {
    $SkillsArgs += "-g"
}

Write-Host "Running: npx skills $($SkillsArgs -join ' ')"
& npx skills @SkillsArgs

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nInstalled. Verify with: npx skills list $(if ($Global) { '-g' }) -a cursor"
} else {
    exit $LASTEXITCODE
}
