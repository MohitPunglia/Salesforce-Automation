# to run .\cleanup.ps1
Write-Host "🧹 Starting deep cleanup process..." -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Cyan

# Remove ALL __pycache__ folders recursively
$pycacheFolders = Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue
foreach ($folder in $pycacheFolders) {
    Remove-Item -Path $folder.FullName -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "✓ Removed: $($folder.FullName)" -ForegroundColor Green
}

# Remove ALL .pyc, .pyo, .pyd files recursively
$pycFiles = Get-ChildItem -Path . -Recurse -File -Filter "*.pyc" -ErrorAction SilentlyContinue
foreach ($file in $pycFiles) {
    Remove-Item -Path $file.FullName -Force -ErrorAction SilentlyContinue
    Write-Host "✓ Removed: $($file.Name)" -ForegroundColor Green
}

$pyoFiles = Get-ChildItem -Path . -Recurse -File -Filter "*.pyo" -ErrorAction SilentlyContinue
foreach ($file in $pyoFiles) {
    Remove-Item -Path $file.FullName -Force -ErrorAction SilentlyContinue
    Write-Host "✓ Removed: $($file.Name)" -ForegroundColor Green
}

$pydFiles = Get-ChildItem -Path . -Recurse -File -Filter "*.pyd" -ErrorAction SilentlyContinue
foreach ($file in $pydFiles) {
    Remove-Item -Path $file.FullName -Force -ErrorAction SilentlyContinue
    Write-Host "✓ Removed: $($file.Name)" -ForegroundColor Green
}

# Remove other cache directories (root level)
$rootItemsToRemove = @(
    ".pytest_cache",
    "allure-results", 
    "allure-report",
    "report.html",
    ".coverage",
    "htmlcov"
)

foreach ($item in $rootItemsToRemove) {
    if (Test-Path $item) {
        Remove-Item -Path $item -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "✓ Removed: $item" -ForegroundColor Green
    }
}

Write-Host "----------------------------------------" -ForegroundColor Cyan
Write-Host "✅ Deep cleanup completed successfully!" -ForegroundColor Green
Write-Host "Removed __pycache__ from all subdirectories" -ForegroundColor Gray