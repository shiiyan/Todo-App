from django import forms

class ToDoListForm(forms.Form):
	text = forms.CharField(max_length=60,
		widget=forms.TextInput(
			attrs={
			"name":"searchbar", "id":"search", "type":"text", "placeholder":"Todoリスト名を入力する" ,"size":"15",
			}))

class ToDoForm(forms.Form):
	text = forms.CharField(max_length=60,
		widget=forms.TextInput(
			attrs={
			"name":"todoname", "type":"text", "placeholder":"Todo名を入力する" ,
			}))
	deadline = forms.DateField(
		widget=forms.TextInput(
			attrs={
			"name": "deadline", "type":"date", "placeholder":"期限を入力する" 
			}))

class SearchForm(forms.Form):
	text = forms.CharField(max_length=60,
		widget=forms.TextInput(
			attrs={"name":"searchbar", "id":"search", "type":"text", "placeholder":"TodoリストまたはTodoを検索する" ,"size":"15",}
			))