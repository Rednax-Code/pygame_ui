
# PygameUI Documentation



```python
Interface.add_element('quit', PygameUI.label(position=[100,100], size=[100,100], text="quit", text_size=5))
```


The following is not required if your program has no interactible elements
```python
for event in pygame.event.get():
	Interface.event_handler(event)
```