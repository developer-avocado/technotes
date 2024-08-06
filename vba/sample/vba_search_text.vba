Sub SearchTextInShapesAllSheets()
    Dim ws As Worksheet
    Dim shp As Shape
    Dim searchText As String
    Dim foundCount As Integer
    Dim sheetFoundCount As Integer
    Dim firstFoundSheet As Boolean
    
    ' 検索する文字列をユーザーに入力してもらう
    searchText = InputBox("検索する文字列を入力してください：")
    
    ' 検索文字列が空の場合は終了
    If searchText = "" Then
        MsgBox "検索文字列が入力されていません。", vbExclamation
        Exit Sub
    End If
    
    foundCount = 0
    firstFoundSheet = True
    
    ' ワークブック内のすべてのシートをループ
    For Each ws In ActiveWorkbook.Worksheets
        sheetFoundCount = 0
        
        ' シート内のすべての図形をループ
        For Each shp In ws.Shapes
            ' 図形にテキストが含まれている場合
            If shp.TextFrame2.HasText Then
                ' 検索文字列が図形のテキストに含まれている場合
                If InStr(1, shp.TextFrame2.TextRange.Text, searchText, vbTextCompare) > 0 Then
                    ' シートが初めて見つかった場合、または既に見つかったシートがある場合
                    If firstFoundSheet Then
                        ws.Activate
                        firstFoundSheet = False
                    End If
                    
                    ' 図形を選択して強調表示
                    shp.Select Replace:=False
                    foundCount = foundCount + 1
                    sheetFoundCount = sheetFoundCount + 1
                End If
            End If
        Next shp
        
        ' シート内で文字列が見つかった場合の情報表示
        If sheetFoundCount > 0 Then
            MsgBox "シート """ & ws.Name & """ 内で文字列 """ & searchText & """ が見つかりました。" & vbNewLine & _
                   "合計 " & sheetFoundCount & " 個の図形で見つかりました。", vbInformation
        End If
    Next ws
    
    ' 検索結果の要約を表示
    If foundCount > 0 Then
        MsgBox "検索完了: " & foundCount & " 個の図形で文字列 """ & searchText & """ が見つかりました。", vbInformation
    Else
        MsgBox "文字列 """ & searchText & """ はすべてのシート内の図形で見つかりませんでした。", vbInformation
    End If
End Sub


