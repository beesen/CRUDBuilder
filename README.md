# CRUDBuilder
## Create CRUD files from Django model

### What is needed to automate creation of files from a Django model?
Assume the app is named "buildings" and the model "Building"
1. Create file "views.py" with BuildingListView, BuildingCreateView, BuildingUpdateView and BuildingDeleteView
2. Create templates in map "templates/buildings": building_list.html, building_form_html, building_confirm_delete.html
3. Create file "urls.py" for the views
