Sub SearchTextBox()
    Dim shp As Shape
    Dim searchText As String
    Dim found As Boolean
    
    searchText = InputBox("検索するテキストを入力してください:")
    found = False
    
    For Each shp In ActiveSheet.Shapes
        If shp.Type = msoTextBox Then
            If InStr(shp.TextFrame2.TextRange.Text, searchText) > 0 Then
                MsgBox "テキストボックス '" & shp.Name & "' にテキストが見つかりました。"
                found = True
                Exit For
            End If
        End If
    Next shp
    
    If Not found Then
        MsgBox "指定したテキストは見つかりませんでした。"
    End If
End Sub
