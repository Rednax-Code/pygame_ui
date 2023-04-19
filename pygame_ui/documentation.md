
# PygameUI Documentation



```python
Interface.add_element('quit', pygame_ui.label(position=[100,100], size=[100,100], text="quit", text_size=5))
```


The following is not required if your program has no interactible elements
```python
for event in pygame.event.get():
	Interface.event_handler(event)
```

```python
Interface.get_path('test_frame').elements
Interface.add_element('test_addition', pygame_ui.frame(is_visible=True), 'test_frame')
Interface.add_element('test_addition_label', pygame_ui.label(is_visible=True), 'test_frame->test_addition')
Interface.remove_element('test_addition_label', 'test_frame->test_addition')
```

```python
sign = Interface.get_element('test_label', 'test_frame->test_frame_in_frame')
sign.text = 'hubba hubba'
```