using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class Draggable : MonoBehaviour, IBeginDragHandler, IDragHandler, IEndDragHandler {

	Vector2 offset;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public void OnBeginDrag(PointerEventData eventData) {
		Debug.Log("on begin drag");

		
		offset = new Vector2(transform.position.x - eventData.position.x, transform.position.y - eventData.position.y);
	}

	public void OnDrag(PointerEventData eventData) {
		Debug.Log("on drag");

		transform.position = new Vector2(eventData.position.x + offset.x, eventData.position.y + offset.y);
	}

	public void OnEndDrag(PointerEventData eventData) {
		Debug.Log("on end drag");
	}	
}
