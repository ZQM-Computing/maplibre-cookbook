// Pattern 08: Custom controls
class MyControl{ onAdd(map){const d=document.createElement('div');d.className='maplibregl-ctrl';d.textContent='X';return d;} onRemove(){} }
map.addControl(new MyControl(),'top-right');
