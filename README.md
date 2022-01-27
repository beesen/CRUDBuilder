# CRUDBuilder
## Create CRUD files from Django model

### What is needed to automate creation of files from a Django model?
Assume the app is named "buildings" and the model "Building"
1. Read the file "models.py" and extract model into list of fields. Each field is represented as a dictionair with "field_name" and "field_type".
2. Create file "views.py" with BuildingListView, BuildingCreateView, BuildingUpdateView and BuildingDeleteView
3. Create templates in map "templates/buildings": building_list.html, building_form_html, building_confirm_delete.html
4. Create file "urls.py" for the views
