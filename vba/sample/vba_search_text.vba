Sub SearchTextInShapes()
    Dim ws As Worksheet
    Dim shp As Shape
    Dim searchText As String
    Dim foundCount As Integer
    
    ' アクティブシートを設定
    Set ws = ActiveSheet
    
    ' 検索する文字列をユーザーに入力してもらう
    searchText = InputBox("検索する文字列を入力してください：")
    
    ' 検索文字列が空の場合は終了
    If searchText = "" Then
        MsgBox "検索文字列が入力されていません。", vbExclamation
        Exit Sub
    End If
    
    foundCount = 0
    
    ' シート内のすべての図形をループ
    For Each shp In ws.Shapes
        ' 図形にテキストが含まれている場合
        If shp.TextFrame2.HasText Then
            ' 検索文字列が図形のテキストに含まれている場合
            If InStr(1, shp.TextFrame2.TextRange.Text, searchText, vbTextCompare) > 0 Then
                ' 図形を選択して強調表示
                shp.Select Replace:=False
                foundCount = foundCount + 1
                
                ' 見つかった図形の情報をメッセージボックスで表示
                MsgBox "文字列 """ & searchText & """ が見つかりました。" & vbNewLine & _
                       "図形名: " & shp.Name & vbNewLine & _
                       "テキスト: " & shp.TextFrame2.TextRange.Text, vbInformation
            End If
        End If
    Next shp
    
    ' 検索結果の要約を表示
    If foundCount > 0 Then
        MsgBox "検索完了: " & foundCount & " 個の図形で文字列 """ & searchText & """ が見つかりました。", vbInformation
    Else
        MsgBox "文字列 """ & searchText & """ は図形内で見つかりませんでした。", vbInformation
    End If
End Sub