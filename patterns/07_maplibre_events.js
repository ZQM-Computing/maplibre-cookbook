// Pattern 07: Advanced event handling
map.on('moveend',()=>console.log('moved',map.getCenter()));
map.on('click','points',e=>{ console.log(e.features[0].properties); });
