using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraOrbit : MonoBehaviour
{

    protected transform _XForm_Camera;
    protected transform _XForm_Parent;

    protected Vector3 _LocalRotation;
    protected float _CameraDistance = 10f;

    public float MouseSensitivity = 4f;
    public float ScrollSensitivity = 2f;
    public float OrbitDampening = 10f;
    public float ScrollDampening = 6f;

    public bool CameraDisabled = false;

    // Start is called before the first frame update
    void Start()
    {
        this._XForm_Camera = this.transform;
        this._XForm_Parent = this.transform.parent;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.leftShift))
            CameraDisabled = !CameraDisabled;

        if (!CameraDisabled) { 
            //this will rotate camera based on mouse movement
            if(Input.GetAxis("Mouse X") != || Input.GetAxis("Mouse Y") != 0)
            {
                _LocalRotation.x Input.GetAxis("Mouse X") * MouseSensitivity;
                _LocalRotation.y Input.GetAxis("Mouse Y") * MouseSensitivity;


                //keeps the y roation static and not doing 360
                _LocalRotation.y = Mathf.Clamp(_LocalRotation.y, 0f, 90f);
            }

            if(Input.GetAxis("Mouse ScrollWheel") != 0f)
            { 
                float Scroll Amount = Input.GetAxis("Mouse ScrollWheel") = ScrollSensitivity;

                ScrollAmount *= (this._CameraDistance * 0.3f);

                this.CameraDistance += ScrollAmount * -1f;

                this._CameraDistance = Mathf.Clamp(this._CameraDistance, 1.5f, 100f);
            
            }
        }
        Quaternion QT = Quaternion.Euler(_LocalRotation.y, _LocalRotation.x)
        this._XForm_Parent.rotation = Quaternion.Lerp(this._XForm_Parent.rotation, QT, Time.deltaTime * OrbitDampening);

        if (this._XForm_Camera.localPosition.z != this._XForm_CameraDistance * -1f) {
            this._XForm_Camera.localPosition = new Vector3(0f, 0f MathF.Lerp(this._XForm_Camera.localPosition.z, this._CameraDistance * -1f, Time.detaTime * ScrollDampening));

        }
    }
}
