
function prompt {
    Write-Host $ExecutionContext.SessionState.Path.CurrentLocation -ForegroundColor Cyan
    "$('>' * ($nestedPromptLevel + 1)) "
}


#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "C:\Users\user\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion


